// A Simple MD Code for Lennard-Jones System
//     mass=1; epsilon=1; sigma=1;
// Version 05: Potential Truncation at RCUT
//             Parallel with OpenMP
// Using Book-keeping Algorithm
//
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>        // OpenMP用ヘッダファイル
#include <time.h>       // 時間計測用

#define NUM_LATTICE  30
#define NUM_ATOM    (NUM_LATTICE*NUM_LATTICE*NUM_LATTICE)

#define TOTAL_STEP  2000
#define SAVE_STEP    100

#define MAX_THREADS  64

#define CUTOFF      3.0
#define DENSITY     0.8

#define MAX_NEIGH   500    // Max Size for Neighbor List
#define BOOK_STEP   100    // List Update Step
#define SKIN        1.0

double DEL_T  = 0.001;
double CELL_X, CELL_Y, CELL_Z; // Cell size is determined by Density

double posx[NUM_ATOM], posy[NUM_ATOM], posz[NUM_ATOM];
double momx[NUM_ATOM], momy[NUM_ATOM], momz[NUM_ATOM];
double frcx[NUM_ATOM], frcy[NUM_ATOM], frcz[NUM_ATOM];
double eng_kin, eng_pot;
double t_target, tsum;
int ntcount;
int num_threads;

int neigh[NUM_ATOM], nlist[NUM_ATOM][MAX_NEIGH];

FILE *fgnuplot, *fsave;

//------------------------------------------------
//   Velocity Scaling
//
void scaling( )
{
   int i;
   double factor;

      factor=sqrt(t_target*NUM_ATOM/tsum);
   for (i=0;i<NUM_ATOM;i++) {
      momx[i] *= factor;
      momy[i] *= factor;
      momz[i] *= factor;
   }

   tsum=0.0;
   ntcount=0;
}
//------------------------------------------------
//   Output Statistical Data & Configuration 
//
void statistics(int step)
{
   int i;
   char fname[100];

      tsum /= ntcount;
   scaling( );

   printf("%8d %10.5f %10.5f %10.5f\n",
      step, eng_kin/NUM_ATOM, eng_pot/NUM_ATOM, (eng_kin+eng_pot)/NUM_ATOM);

      sprintf(fname,"lj%8.8d.dat",step);
      fsave=fopen(fname,"w");
      fprintf(fsave,"%f %f %f\n",CELL_X,CELL_Y,CELL_Z);
   for (i=0;i<NUM_ATOM;i++) {
      fprintf(fsave,"%8.3f %8.3f %8.3f  ",posx[i],posy[i],posz[i]);
      fprintf(fsave,"%8.3f %8.3f %8.3f\n",momx[i],momy[i],momz[i]);
   }
      fclose(fsave);

      fprintf(fgnuplot,"plot \"%s\" using 1:2 t \"%5.5d\" w po pt 6\n",fname,step);
   if (step==0) {
      fprintf(fgnuplot,"pause -1\n");
   } else {
      fprintf(fgnuplot,"pause 0.01\n");
   }
}
//------------------------------------------------
//   Initialize Gnuplot Command File
//
void initplot( )
{
   fgnuplot=fopen("lj.plt","w");

   fprintf(fgnuplot,"set size square\n");
   fprintf(fgnuplot,"set key out\n");
   fprintf(fgnuplot,"set xran [0:%f]\n",CELL_X);
   fprintf(fgnuplot,"set yran [0:%f]\n",CELL_Y);
}
//------------------------------------------------
//   Finalize Gnuplot Command File
//
void finalplot( )
{
   fclose(fgnuplot);
}
//------------------------------------------------
//   Make Simple Cubic Lattice with Random Momenta
//
void initial( )
{
   int i=0;
   int ix,iy,iz;
   double dx,dy,dz;

   CELL_X=pow(DENSITY, -1.0/3.0)*NUM_LATTICE;
         printf("CELL Size = %12.4f\n",CELL_X);
      if (CELL_X < 2*CUTOFF) {
         printf("Waring: CUTOFF should be less than half of CELL Size\n");
      }
   CELL_Y=CELL_Z=CELL_X;

      dx=CELL_X/NUM_LATTICE;
      dy=CELL_Y/NUM_LATTICE;
      dz=CELL_Z/NUM_LATTICE;

      tsum=0.0;

   for (ix=0;ix<NUM_LATTICE;ix++) {
   for (iy=0;iy<NUM_LATTICE;iy++) {
   for (iz=0;iz<NUM_LATTICE;iz++) {
      posx[i] = dx*ix;
      posy[i] = dy*iy;
      posz[i] = dz*iz;
      momx[i] = (rand( )/(double)RAND_MAX -0.5);
      momy[i] = (rand( )/(double)RAND_MAX -0.5);
      momz[i] = (rand( )/(double)RAND_MAX -0.5);
         tsum += (momx[i]*momx[i]+momy[i]*momy[i]+momz[i]*momz[i]);
      i++;
   } } }

      tsum /= 2;
      scaling( );
}
//------------------------------------------------
//   Neighbor List Update
//
void list_update( )
{
   int i, j, in;
   double dx,dy,dz,r2;
   double cxh=CELL_X/2;
   double cyh=CELL_Y/2;
   double czh=CELL_Z/2;
   double RTBL2=(CUTOFF+SKIN)*(CUTOFF+SKIN);

#pragma omp parallel for private (i,j,in,dx,dy,dz,r2)
   for (i=0; i<NUM_ATOM; i++) {
      in=0;

   for (j=i+1; j<NUM_ATOM; j++) {
      dx=posx[i]-posx[j];
         if (dx<-cxh) dx+=CELL_X;
         else if (dx>cxh) dx-=CELL_X;
      dy=posy[i]-posy[j];
         if (dy<-cyh) dy+=CELL_Y;
         else if (dy>cyh) dy-=CELL_Y;
      dz=posz[i]-posz[j];
         if (dz<-czh) dz+=CELL_Z;
         else if (dz>czh) dz-=CELL_Z;
      r2=dx*dx+dy*dy+dz*dz;
      if (r2<RTBL2) {
         nlist[i][in]=j;
         in++;
         if (in==MAX_NEIGH) {
            printf("Warning: Number of Neibors exceeds MAX_NEIGH\n");
            in--;
         }
      }
   }
      neigh[i]=in;
   }

   // printf("Neighbor List Updated\n");
}
//------------------------------------------------
//   Calculate Forces: minimal image convention
//
void force( )
{
   int i, j, in, th;
   double dx,dy,dz,r2,ri06,ri12;
   double eng, frc;
   double cxh=CELL_X/2;
   double cyh=CELL_Y/2;
   double czh=CELL_Z/2;
   double RCUT2=CUTOFF*CUTOFF;
   double fix,fiy,fiz;
   static double fx[MAX_THREADS][NUM_ATOM], fy[MAX_THREADS][NUM_ATOM], fz[MAX_THREADS][NUM_ATOM];

      eng_pot=0.0;
#pragma omp parallel for private (i,th)
   for (i=0; i<NUM_ATOM; i++) {
      frcx[i]=frcy[i]=frcz[i]=0.0;
   for (th=0;th<num_threads;th++) {
      fx[th][i]=0.0;
      fy[th][i]=0.0;
      fz[th][i]=0.0;
   } }

#pragma omp parallel for private (i,in,j,th,dx,dy,dz,r2,ri06,ri12,eng,frc) reduction(+:eng_pot) 
   for (i=0; i<NUM_ATOM; i++) {
         th=omp_get_thread_num();
   for (in=0; in<neigh[i]; in++) {   // Refer Neighbor List
      j=nlist[i][in];

      dx=posx[i]-posx[j];
         if (dx<-cxh) dx+=CELL_X;
         else if (dx>cxh) dx-=CELL_X;
      dy=posy[i]-posy[j];
         if (dy<-cyh) dy+=CELL_Y;
         else if (dy>cyh) dy-=CELL_Y;
      dz=posz[i]-posz[j];
         if (dz<-czh) dz+=CELL_Z;
         else if (dz>czh) dz-=CELL_Z;
      r2=dx*dx+dy*dy+dz*dz;
      if (r2<RCUT2) {
         ri06=1.0/(r2*r2*r2);
         ri12=ri06*ri06;

         eng=4*(ri12-ri06);
         frc=4*(12*ri12-6*ri06)/r2;

         eng_pot += eng;

         frcx[i] += frc*dx;
         frcy[i] += frc*dy;
         frcz[i] += frc*dz;
         fx[th][j] -= frc*dx;
         fy[th][j] -= frc*dy;
         fz[th][j] -= frc*dz;
      }
   }
   }

#pragma omp parallel for private (i,th)
   for (i=0; i<NUM_ATOM; i++) {
   for (th=0; th<num_threads; th++) {
      frcx[i]+=fx[th][i];
      frcy[i]+=fy[th][i];
      frcz[i]+=fz[th][i];
   } }
}
//------------------------------------------------
//   Update Particle Positon & Momentum: Periodic Boundaries
//
void move( )
{
   int i;

      eng_kin=0.0;

#pragma omp parallel for private (i) reduction(+:eng_kin)
   for (i=0; i<NUM_ATOM; i++) {
      momx[i] += frcx[i]*DEL_T;
      momy[i] += frcy[i]*DEL_T;
      momz[i] += frcz[i]*DEL_T;
         eng_kin += (momx[i]*momx[i]+momy[i]*momy[i]+momz[i]*momz[i]);

      posx[i] += momx[i]*DEL_T;
         if (posx[i]<0.0)         posx[i]+=CELL_X;
         else if (posx[i]>CELL_X) posx[i]-=CELL_X;
      posy[i] += momy[i]*DEL_T;
         if (posy[i]<0.0)         posy[i]+=CELL_Y;
         else if (posy[i]>CELL_Y) posy[i]-=CELL_Y;
      posz[i] += momz[i]*DEL_T;
         if (posz[i]<0.0)         posz[i]+=CELL_Z;
         else if (posz[i]>CELL_Z) posz[i]-=CELL_Z;
   }
      eng_kin /= 2;

      ntcount++;
      tsum += (2.0/3.0)*eng_kin;
}

//***************************************************************
int main( )
{
   int step;
   clock_t t1,t2;
   double to1,to2;

      printf("Input Target Temperature :");
      scanf("%lf",&t_target);

#pragma omp parallel
   {  num_threads=omp_get_num_threads();}
      printf("This code is working on %2d nodes\n",num_threads);

      initial( );
      initplot( );

      t1=clock( );
      to1=omp_get_wtime( );
   for (step=0; step<=TOTAL_STEP; step++) {
      if (step%BOOK_STEP==0) {
         list_update( );
      }
      force( );
      move( );
      if (step%SAVE_STEP==0) {
         statistics(step);
      }
   }

      t2=clock( );
      to2=omp_get_wtime( );
      printf("CPU Time: %10.5f s on %3d nodes\n",(double)(t2-t1)/CLOCKS_PER_SEC,num_threads);
      printf("Wall Time: %10.5f s on %3d nodes\n",to2-to1,num_threads);

      finalplot( );
}
