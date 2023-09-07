#include <stdio.h>
#include <math.h>

#define DFILE "StyleOfPollock2021_large"  // ���͗p�摜�t�@�C�����i�g���q .bmp �͎����I�ɕt���j
#define DMAX  65536   // Maximum header size
#define IMAX   4800   // Maximum image size

int Width, Height;
int Image[IMAX][IMAX];
int Threshold;

int read_image(char* INPUT_FILE ) //=====================================================
{
   FILE *fin;
   unsigned char cdata[DMAX];
   unsigned int Offset, HeaderSize;
   unsigned short int NBit, NByte, dummy;
   unsigned int Cmprs;
   unsigned int idata;
   int x,y,xmax,r,g,b;

   fin=fopen(INPUT_FILE,"rb");
   if (fin==NULL) {
      printf("Error: no input file: %s\n",INPUT_FILE);
      return -1;
   }
   printf("Analyzing %s\n",INPUT_FILE);

// Bitmap File Header             �摜�t�@�C���̃w�b�_���𒲂ׂ�
   fread(cdata,10,1,fin);
   printf("File Type = %c%c\n",cdata[0],cdata[1]);
   if (cdata[0]!='B' || cdata[1]!='M') {
      printf("Error: file is not BMP\n");
      fclose(fin);
      return -1;
   }
   fread(&Offset,4,1,fin);

// Bitmap Info Header
   fread(&HeaderSize,4,1,fin);
   printf("Header Size = %d byte\n",HeaderSize);
   printf("Offset = %d byte\n",Offset);
   fread(&Width,4,1,fin);
   fread(&Height,4,1,fin);
   fread(&dummy,2,1,fin);
   fread(&NBit,2,1,fin);
   fread(&Cmprs,4,1,fin);
   printf("Image Size = %d X %d\n",Width,Height);
   printf("Image = %2d bit/pixel\n",NBit);
      NByte=NBit/8;
   printf("Compress Mode = %d\n",Cmprs);
   if (Cmprs!=0) {      // ���̃v���O�����͖����k bitmap (Mode=0) �݂̂ɑΉ����Ă���
      printf("Sorry, this program does not support this compression type\n");
      fclose(fin);
      return -1;
   }
   if (NBit<=4) {
      printf("Sorry, this program does not support this Pixel Bit type\n");
      return -1;
   }
   if ((Width>IMAX) || (Height>IMAX)) {
      printf("Sorry, the image is too large\n");
      fclose(fin);
      return -1;
   }
   fclose(fin);

//   return 9;   // For Debugging

   fin=fopen(INPUT_FILE,"rb");   // �摜�t�@�C�����J�������āC�摜�f�[�^��ǂݍ���
   fread(cdata,Offset,1,fin);

// Read Image
   for (y=0;y<Height;y++) {
      for (x=0;x<Width;x++) {
         idata=(unsigned int)0;
         int status=fread(&idata, NByte, 1, fin); // �s�N�Z���f�[�^�ǂݍ���
         if (status!=1) {
            printf("Error at %d %d: data end while reading\n",x,y);
            return -1;
         }
         b=idata%256; idata/=256;  // NByte�̉�f�f�[�^��rgb�l�ɕϊ�
         g=idata%256; idata/=256;
         r=idata;
         // printf("%5d %5d | %3d %3d %3d\n",x,y,r,g,b);
         if (r+g+b<3*Threshold) Image[y][x] = 0;   // Threshold �łQ�l��
         else                   Image[y][x] = 1;
      }
         xmax=(Width*NByte)%4;
      for (x=0;x<xmax;x++) fread(&idata, 1, 1, fin);
       // ���������̃o�C�g����4�̔{���łȂ��ꍇ�́C0x0 �Ŗ��߂��Ă���̂œǂݔ�΂�
   }

   fclose(fin);
   return 0;
}

int fractal( ) //=============================
{
   int x, y, xtile, ytile;
   int resolution;       // Tile Size
   int sum;              // Number of Tiles
   int res_max;
   int black, white;
   char cname[100];
   FILE *fout;

   sprintf(cname,"%s_%3.3d.dat",DFILE,Threshold);  // �o�͗p�t�@�C����
   fout=fopen(cname,"w");

   if (Height<Width) res_max=Height/2;   // �^�C���̍ő�T�C�Y��ݒ�
   else              res_max=Width/2;

   for (resolution=2; resolution<=res_max; resolution*=2) { // タイルサイズを２倍ずつ大きくする
      sum=0;         // 「条件」に合致するタイルの枚数 sum を初期化
      for (ytile = 0; ytile < Height/resolution; ytile++) {  // タイルを１枚ずつチェックしていく
         for (xtile = 0; xtile < Width/resolution;  xtile++) {
            black = 0;
            white = 0;
            for (y = resolution*ytile;y < resolution*(ytile+1);y++){
               for (x = resolution*xtile;x < resolution*(xtile+1);x++){
                  if (Image[y][x] == 0){
                     black++;
                  }
                  else {
                     white++;
                  }
               }
            }
            if (white>0 && black>0){
               sum++;
            }            
         }
      }
      fprintf(fout,"%5d %10d\n", resolution, sum);  // タイルの枚数を出力
      printf("%5d %10d\n", resolution, sum);
   }

   fclose(fout);
   return 0;
}

int main( ) //=================================================
{
   int ret;
   
   char cfile[100];
   FILE *fout;

   printf("Input Threshold (<=255):"); // ���̒l�ȉ����u���v�Ɣ��肷��
   scanf("%d",&Threshold);

      sprintf(cfile,"%s.bmp",DFILE);
   ret=read_image(cfile);
   if (ret!=0) return -1;

   fractal( );

   return 0;
}
