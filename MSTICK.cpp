#include<iostream>
#include<cstdio>
#include<bits/stdc++.h>

using namespace std;
typedef long long int ll;

const int N = 1e5;  // limit for array size
ll n;  // array size
ll t1[2*N];
ll t2[2*N];

void build1() {  // build the tree
  for (int i=n-1; i>0; --i) t1[i] = min(t1[i<<1], t1[i<<1|1]);
}

ll query1(int l, int r) {  // sum on interval [l, r) using 0 based index
  ll res = 100000000;
  for (l+=n, r+=n; l<r; l>>=1, r>>=1) {
    if (l&1) res = min(res, t1[l++]);
    if (r&1) res = min(res, t1[--r]);
  }
  return res;
}

void build2(){  // build the tree
  for (int i=n-1; i>0; --i) t2[i] = max(t2[i<<1], t2[i<<1|1]);
}

int query2(int l, int r) {  // sum on interval [l, r) using 0 based index
  ll res = 0;
  for(l+=n, r+=n; l<r; l>>=1, r>>=1) {
    if (l&1) res = max(res, t2[l++]);
    if (r&1) res = max(res, t2[--r]);
  }
  return res;
}

int main(){
    ll q;
    cin>>n;
    for(int i = 0; i < n; ++i){
        cin>>t1[n+i];
        t2[n+i] = t1[n+i];
    }
    build1();
    build2();
    cin>>q;
    //cout<<query1(4, 11);
    while(q--){
        ll l, r;
        cin>>l>>r;
        double mn = query1(l, r+1); //min element in range(l, r+1)
        double mx = max(query2(0, l), query2(r+1, n)); //max element in range(0,n)- range(l, r+1)
        double mxt = query2(l, r+1);
        double ans = max(mn+mx, mn + (mxt-mn)/2);
        printf("%.1f\n", ans);//<<mn<<mx<<mxt;
    }
    //printf("%d\n", query(3, 11));
    return 0;
}

