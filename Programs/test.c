#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//構造体宣言
struct build{
    char name[128];//char型
    float math;//float型
    float english;//float型
    float avg;//float型
};
int main(void)
{
	struct build p[3];// 構造体配列の宣言
	strcpy(p[0].name, "鈴木");// 配列の0番目の要素の各メンバ
	p[0].math = 85;
	p[0].english = 50;
	p[0].avg = 0;
	strcpy(p[1].name, "佐藤");// 配列の1番目の要素の各メンバ
	p[1].math = 75;
	p[1].english = 70;
	p[1].avg = 0;
	strcpy(p[2].name, "高橋");// 配列の2番目の要素の各メンバ
	p[2].math = 90;
	p[2].english = 65;
	p[2].avg = 0;
	//for 文を用いて，各学生の平均点を計算し，対応するメンバに代入する．
	for(int a=0;a<3;a++){
	   	p[a].avg=(p[a].math+p[a].english)/2;
	}
	FILE *fp;
	fp = fopen("output.bin", "ab+");
	fwrite(p, sizeof(struct build), 3, fp);
	fclose(fp);
	return EXIT_SUCCESS;
}