// �Q�����u���E���^���̋O�Ղ�ǐՂ���Fver. 2
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define mass      1.0      // ���q����
#define gamma     1.0      // ���C�W��
#define c_rand    1.0      // �����_���͂̑傫��
#define delta_t   0.1      // ���ԍ���˜˜≠˜
#define total_step 5000000    // �v�Z�X�e�b�v��

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
   FILE *fout;

      fout = fopen("brown.dat","w");
      if (fout==NULL) {        // �G���[�`�F�b�N
         printf("Error: cannot open file\n");
         return -1;
      }
      x=0.0; y=0.0;
      u=0.0; v=0.0;
   for (step=0; step<total_step; step++) {
      printf("%7.2f %10.3f %10.3f %10.3f %10.3f\n",step*delta_t,x,y,u,v);
      fprintf(fout,"%7.2f %12.5f %12.5f %12.5f %12.5f\n",step*delta_t,x,y,u,v);
      x += delta_t * u;
      y += delta_t * v;
      u += delta_t/mass * (-gamma*u + fr( )); 
      v += delta_t/mass * (-gamma*v + fr( ));
   }
      fclose(fout);
   return 0;
}
