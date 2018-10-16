#include<iostream>
using namespace std;
main(){
    int t;
    cin>>t;
    while(t--){
        int n, m;
        cin>>n>>m;
        char gift[n][m+1];
        for(int i=0; i<n; i++)
            cin>>gift[i];
        int s1 = 0, s2 = 0;
        for(int i=0; i<n; i++){
            if(i%2==0){
                for(int j = 0; j<m; j++){
                    if(j%2==0){
                        if(gift[i][j]=='G')    s1+=3;
                        else    s2+=5;
                    }
                    else{
                        if(gift[i][j]=='R')    s1+=5;
                        else    s2+=3;
                    }
                }
            }
            else{
                for(int j = 0; j<m; j++){
                    if(j%2==0){
                        if(gift[i][j]=='G')    s2+=3;
                        else    s1+=5;
                    }
                    else{
                        if(gift[i][j]=='R')    s2+=5;
                        else    s1+=3;
                    }
                }
            }
        }
        if(s1<s2) cout<<s1<<endl;
        else cout<<s2<<endl;
    }
}
