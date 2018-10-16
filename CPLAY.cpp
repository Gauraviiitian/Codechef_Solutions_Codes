#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

main(){
    string p;
    while(getline(cin, p) && p.length()){
        int i = 0, score_a = 0, score_b = 0, f = 0, rem_a = 5, rem_b = 5;
        for(i=0; i<20; i++){
            if(i%2==0){
                if(p[i]=='1')    score_a++;
                rem_a--;
            }
            if(i%2==1){
                if(p[i]=='1')    score_b++;
                rem_b--;
            }
            if(score_a>score_b && i>=10 && i%2==1){
                f = 1;
                break;
            }
            if(score_b>score_a && i>=10 && i%2==1){
                f = 2;
                break;
            }
            if(i<10 && score_a>score_b+rem_b){
                f=1;
                break;
            }
            if(i<10 && score_b>score_a+rem_a){
                f=2;
                break;
            }
        }
        if(f==1)
            printf("TEAM-A %d\n", i+1);
        else if(f==2)
            printf("TEAM-B %d\n", i+1);
        else
            printf("TIE\n");
    }
}
