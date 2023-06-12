// �Q�����u���E���^���̑��x���ȑ��֊֐�
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define mass      1.0      // ���q����
#define gamma     1.0      // ���C�W��
#define c_rand    1.0      // �����_���͂̑傫��
#define delta_t   0.01      // ���ԍ���

#define total_step 100000  // �v�Z�X�e�b�v��
#define vaf_step  1000     // �o�̓X�e�b�v��

double fr( )
{
   double factor;

   factor=sqrt((3*c_rand)/(2*delta_t));
   return ( rand( )/(double)RAND_MAX*2 - 1.0 ) * factor;
}

int main( )
{
   double x, y;
   double u, v;
   int step;
   FILE *fvaf;

   int i, j;
   double dx, dy;
   static int count[vaf_step];
   static double vaf[vaf_step];
   static double velx[total_step], vely[total_step];

      fvaf = fopen("vaf.dat","w");
      if (fvaf==NULL) {
         printf("Error: cannot open file\n");
         return -1;
      }

      x=0.0; y=0.0;
      u=0.0; v=0.0;

   for (step=0; step<total_step; step++) {
//    printf("%7.2lf %10.3lf %10.3lf %10.3lf %10.3lf\n",step*delta_t,x,y,u,v);
      x += delta_t * u;
      y += delta_t * v;
      u += delta_t/mass * (-gamma*u + fr( )); 
      v += delta_t/mass * (-gamma*v + fr( ));
      velx[step]=u;
      vely[step]=v;
   }

   for (step=0; step<vaf_step; step++) {   // �J�E���^������
      count[step]=0;
      vaf[step]=0;
   }

   for (i=0; i<total_step; i++) {   // ���x���ȑ��֊֐��̌v�Z
      for (j=i; j<total_step; j++) {
         step=j-i;
         if (step>vaf_step){
            break; }
         count[step]++;
         vaf[step]+=velx[i]*velx[j]+vely[i]*vely[j];
      }
   }

   for (step=0; step<vaf_step; step++) {
      fprintf(fvaf, "%10.3lf %10.3lf\n", delta_t*step, vaf[step]/count[step]);
   }
      fclose(fvaf);

   return 0;
}