#include <iostream>
#include <bits/stdc++.h>

typedef long long int ll;

#define MAXN 1000007
using namespace std;

const int mod = 1e9 + 7;
const int INF = 1 << 27;
ll tree[2*MAXN];
int spf[MAXN];
int n, m, l, r;
int arr[MAXN];

void sieve(){
    spf[1] = 1;
    for (int i=2; i<MAXN; i++)
        spf[i] = i;
    for (int i=4; i<MAXN; i+=2)
        spf[i] = 2;
    for (int i=3; i*i<MAXN; i++){
        if (spf[i] == i){
            for (int j=i*i; j<MAXN; j+=i)
                if (spf[j]==j)
                    spf[j] = i;
        }
    }
}

void build() {  // build the tree
    for (int i=0; i<n; ++i) tree[n+i] = max(1, spf[arr[i]]);
    for (int i=n-1; i>0; --i) tree[i] = max(tree[i<<1], tree[i<<1|1]);
}

void update(int node, int a, int b, int l, int r){
	if(a>b || a>r || b<l) // Current segment is not within range [i, j]
		return;
    if(tree[node]==1)
        return;
  	if(a==b) { // Leaf node
    	int temp=arr[a];
    	if(spf[temp]!=0)
            arr[a]=temp/spf[temp];
            tree[node]=max(1, spf[arr[a]]);
    	return;
	}
    update(node*2, a, (a+b+1)/2,l,r); // Updating left child
    update(1+node*2, 1+(a+b+1)/2, b,l,r); // Updating right child
    tree[node] = max(tree[node*2], tree[node*2+1]);// Updating root with max value
}

int query(int node, int a, int b) {
	if(a>b || a>r || b<l)
	    return -INF; // Out of range

    if(tree[node]==1)
        return 1;

	if(a>=l && b<=r) // Current segment is totally within range [i, j]
	    return tree[node];

	int q1 = query(node*2, a, (a+b)/2); // Query left child
	int q2 = query(1+node*2, 1+(a+b)/2, b); // Query right child
	return max(q1, q2);
}

int main(){
    sieve();
    //for(int i=0; i<20; i++) cout<<spf[i]<<" ";
    ll t;
    cin>>t;
    while(t--){
        cin>>n>>m;
        for(int i=0; i<n; i++) cin>>arr[i];
        build();
        for(int i=0; i<2*n; i++) cout<<tree[i]<<" ";
        while(m--){
            int tp;
            cin>>tp>>l>>r;
            l--; r--;
            if(tp==1) ;//cout<<query(1, 0, n-1)<<" ";
            else update(1, 0, n-1, l, r);
            cout<<"tree   : ";
            for(int i=0; i<2*n; i++) cout<<tree[i]<<" ";
            cout<<"\n";
        }
        cout<<"\n";
    }
	// your code goes here
	return 0;
}
