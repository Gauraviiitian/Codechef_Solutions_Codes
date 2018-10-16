#include<iostream>
#include<cstdio>
#include<bits/stdc++.h>

using namespace std;

typedef long long int ll;

const int N = 1e5;  // limit for array size
int n;  // array size
ll t[2*N];
multiset<int> s[4*N];

void build() {  // build the tree
  for (int i=n-1; i>0; --i) t[i] = max(t[i<<1], t[i<<1|1]);
}

void modify(int p, int value) {  // set value at position p using 0 based index
  for (t[p+=n]=value; p>1; p>>=1) t[p>>1] = min(t[p], t[p^1]);
}

int query(int l, int r) {  // sum on interval [l, r) using 0 based index
    int res = 100000000;
    for (l+=n, r+=n; l<r; l>>=1, r>>=1){
        if (l&1) res = min(t[l++], res);
        if (r&1) res = min(t[--r], res);
    }
    return res;
}

int main(){
    int t;
    cin>>t;
    while(t--){
        int q;
        cin>>n>>q;
        for(int i=0; i<n; ++i) cin>>t[n+i];
        build();
        while(q--){
            int t, l, r;
            cin>>t>>l>>r;
            if(t==1) cout<<query(l, r+1)<<endl;
            else modify(l, r);
        }
    }
    return 0;
}
