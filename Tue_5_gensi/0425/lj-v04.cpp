//
// A Simple MD Code for Lennard-Jones System
//     mass=1; epsilon=1; sigma=1;
// Version 04: Add Pressure Calculation
//
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM_LATTICE   5
#define NUM_ATOM    (NUM_LATTICE*NUM_LATTICE*NUM_LATTICE)

#define TOTAL_STEP  60000
#define SAVE_STEP   100

double DEL_T  = 0.001;
double uehira =10.0;
double CELL_X =  uehira;
double CELL_Y =  uehira;
double CELL_Z =  uehira;

void initial( );            // Function Prototypes
void force( );
void move( );
void statistics(int);
void initplot( );
void finalplot( );
void scaling( );

double posx[NUM_ATOM], posy[NUM_ATOM], posz[NUM_ATOM];
double momx[NUM_ATOM], momy[NUM_ATOM], momz[NUM_ATOM];
double frcx[NUM_ATOM], frcy[NUM_ATOM], frcz[NUM_ATOM];
double eng_kin, eng_pot, virial;
double t_target, tsum;
double psum;
int ntcount, npcount;

FILE *fgnuplot, *fsave, *fstat;

int main( )
{
   int step;

      printf("Input Target Temperature :");
      scanf("%lf",&t_target);

      fstat=fopen("lj-energy.dat","w");
      initial( );
      initplot( );
   
   for (step=0; step<=TOTAL_STEP; step++) {
      force( );
      move( );
      if (step%SAVE_STEP==0) statistics(step);
   }

      finalplot( );
      printf("\nMean Pressure = %14e\n",psum/npcount);
      fclose(fstat);
   return 0;
}

//------------------------------------------------
//   Initialize Gnuplot Command File
//
void initplot( )
{
   fgnuplot=fopen("lj.plt","w");

   fprintf(fgnuplot,"set size square\n");
   fprintf(fgnuplot,"set xran [0:%f]\n",CELL_X);
   fprintf(fgnuplot,"set yran [0:%f]\n",CELL_Y);
}
//------------------------------------------------
//   Finalize Gnuplot Command File
//
void finalplot( )
{
//   fprintf(fgnuplot,"pause -1\n");
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

      npcount=0;
      psum=0.0;
}
//------------------------------------------------
//   Calculate Forces: minimal image convention
//
void force( )
{
   int i, j;
   double dx,dy,dz,r2,ri06,ri12;
   double eng, frc;
   double cxh=CELL_X/2;
   double cyh=CELL_Y/2;
   double czh=CELL_Z/2;

      eng_pot=0.0;
      virial=0.0;
   for (i=0; i<NUM_ATOM; i++) {
      frcx[i]=0.0;
      frcy[i]=0.0;
      frcz[i]=0.0;
   }

   for (i=0; i<NUM_ATOM; i++) {
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
      ri06=1.0/(r2*r2*r2);
      ri12=ri06*ri06;

      eng=4*(ri12-ri06);
      frc=4*(12*ri12-6*ri06)/r2;

      eng_pot += eng;
      virial += frc*r2;
      frcx[i] += frc*dx;
      frcy[i] += frc*dy;
      frcz[i] += frc*dz;
      frcx[j] -= frc*dx;
      frcy[j] -= frc*dy;
      frcz[j] -= frc*dz;
   } }
}
//------------------------------------------------
//   Update Particle Positon & Momentum: Periodic Boundaries
//
void move( )
{
   int i;

      eng_kin=0.0;

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
//------------------------------------------------
//   Output Statistical Data & Configuration 
//
void statistics(int step)
{
   int i;
   double press;
   char fname[100];

      press=( (2.0/3.0)*eng_kin + (1.0/3.0)*virial )/(CELL_X*CELL_Y*CELL_Z);
   printf("%8d %10.5f %10.5f %10.5f %14.5e\n",
      step, eng_kin/NUM_ATOM, eng_pot/NUM_ATOM, 
      (eng_kin+eng_pot)/NUM_ATOM, press);
   fprintf(fstat,"%8d %10.5f %10.5f %10.5f %14.5e\n",
      step, eng_kin/NUM_ATOM, eng_pot/NUM_ATOM, 
      (eng_kin+eng_pot)/NUM_ATOM, press);

      tsum /= ntcount;
   scaling( );

   if (step>TOTAL_STEP/2) {
      psum += press;
      npcount++;
   }

      sprintf(fname,"lj%8.8d.dat",step);
      fsave=fopen(fname,"w");
   for (i=0;i<NUM_ATOM;i++) {
      fprintf(fsave,"%8.3f %8.3f %8.3f\n",posx[i],posy[i],posz[i]);
   }
      fclose(fsave);

      fprintf(fgnuplot,"plot \"%s\" using 1:2 t \"%5.5d\" w po pt 6 ps 2 lw 2\n",fname,step);
   if (step==0) {
      fprintf(fgnuplot,"pause -1\n");
   } else {
      fprintf(fgnuplot,"pause 0.01\n");
   }
}
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
