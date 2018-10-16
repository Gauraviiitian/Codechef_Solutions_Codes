#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int n;
    cin>>n;
    int matrix[n][n];
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin>>matrix[i][j];
        }
    }
    int sum1=0, sum2=0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(i==j)
                sum1 += matrix[i][j];
            if(i+j == n-1)
                sum2 += matrix[i][j];
        }
    }
    int d = abs(sum1-sum2);
    cout<<d<<"\n";
    return 0;
}
