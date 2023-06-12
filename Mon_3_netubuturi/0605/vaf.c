// ２次元ブラウン運動の速度自己相関関数を求める
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define mass     1.0        // 粒子質量
#define gamma    1.0        // 摩擦係数
#define c_rand   1.0        // ランダム力の大きさ
#define delta_t  0.01       // 時間刻み
#define total_step   100000 // 計算ステップ数
#define out_step  1000      // VAFの出力ステップ数

double fr( )                 // 0以上1以下の一様乱数
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
   int i, j;
   int count[out_step];
   double vaf[out_step];
   static double velx[total_step], vely[total_step];  // 大きなサイズを扱えるよう static に

      x=0.0; y=0.0;			// 初期条件：原点から初速度ゼロで出発
      u=0.0; v=0.0;
   for (step=0; step<total_step; step++) {
      x += delta_t * u;
      y += delta_t * v;
      u += delta_t/mass * (-gamma*u + fr( )); 
      v += delta_t/mass * (-gamma*v + fr( ));
      velx[step]=u;			// 速度データを配列に格納する
      vely[step]=v;
   }

   for (step=0; step<out_step; step++) {	// カウンタ初期化
      count[step]=0;
      vaf[step]=0.0;
   }
   for (i=0; i<total_step; i++) { 		// 速度自己相関関数の計算
      for (j=i; j<total_step; j++) {
         step=j-i;
         if (step>out_step){
            break;
         }
         count[step]++;
         vaf[step]+=velx[i]*velx[j]+vely[i]*vely[j];
      }
   }

   fout = fopen("vaf.dat","w");
   for (step=0; step<out_step; step++) {	// 結果をファイルに出力
      fprintf(fout, "%10.3f %10.3f\n", delta_t*step, vaf[step]/count[step]);
   }
   fclose(fout);

   fout = fopen("vaf.csv","w");
   for (step=0; step<out_step; step++) {  // 結果をファイルに出力
      fprintf(fout, "%10.3f,%10.3f\n", delta_t*step, vaf[step]/count[step]);
   }
   fclose(fout);

   return 0;
}