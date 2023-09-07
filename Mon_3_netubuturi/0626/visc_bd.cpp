// �Q�d��˒��̔S���x�z�u���E���^��
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <cstdlib>  // abs() for integer
#include <cmath> 

#define gamma        1.0       // ���C�W��
#define delta_t      0.0002   // ���ԍ���
#define TOTAL_STEP   1000000   // �v�Z�X�e�b�v���C�����Ƒ��₵�Ă�����
#define SAVE_STEP    10        // �t�@�C���o�͕p�x

//---------------------------------------------------------
double fr(double factor)     // ��l��������
{
   return ( rand( )/(double)RAND_MAX*2 - 1.0 ) * factor;
}
//---------------------------------------------------------
double potential(double x)   // �|�e���V�����G�l���M�[�C�v�Z�̒��ł͎g��Ȃ�
{
   double x2;
   x2=x*x;
   return (0.01*x2*x2 - 3.0)*x2;
}
//---------------------------------------------------------
double force(double x)       // �|�e���V������
{
   double x2;
   x2=x*x;
   return (-0.06*x2*x2 + 6.0)*x;
}
//---------------------------------------------------------
int main( )
{
   double x,x1;
   double factor, temperature;
   int step,n;
   FILE *fout;

   fout = fopen("visc_bd.dat","w");

   temperature= 5000.0;            // ���낢��ȁu���x�v�Ōv�Z����
   factor=sqrt((3*2*temperature)/delta_t);

      n = 0;
      x=-4.0;                 // �����ʒu�͍��̒J�̋߂� -4.0 �ɌŒ�
   for (step=0; step<=TOTAL_STEP; step++) {
      if (step%SAVE_STEP == 0) {
         printf("%9d %10.3f\n",step,x);
         fprintf(fout,"%9d %10.3f\n",step,x);
         x1 = x;
      }
      if ((x1*x > 0) & (abs(x1-x)>1)){
          n =n+1;
      }
      x+= delta_t * (force(x)+fr(factor))/gamma;
   }

   fclose(fout);
   printf("%d\n",n);
   return 0;
}
