#include <bits/stdc++.h> 
using namespace std;
 
typedef long long ll;

const int MOD = 1e9 + 7;
double EPS = 1e-9;
int INF = 1000000005;
long long INFF = 1000000000000000005ll;
double PI = acos(-1);
 
#define all(v) v.begin(), v.end() // all elements in a vector
#define alla(arr, sz) arr, arr + sz // all elements in an array
#define mine *min_element // min element 
#define maxe *max_element // max element 

#define nl '\n'; // newline

// Print 1D/2D array/vector for debugging
#define print1(a, n) for(int i=0;i<n;++i){cout<<a[i]<<' ';}cout<<nl;
#define print2(a, m, n) for(int i=0;i<m;++i){for(int j=0;n;++j)\
{cout<<a[i][j]<<' ';}cout<<nl;}

///////////////////////////////////////////////////////////////////////////////
 
const int MAXN = 1e6+1;
ll dp[MAXN] = {0};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll n, x; cin >> n >> x;
    vector<int> coins(n);
    for (int i = 0; i < n; ++i) {
        cin >> coins[i];
    }

    dp[0] = 0;
    for (int i = 1; i <= x; ++i) {
        ll curr = INF; // current min number of coins from subproblem
        for (auto coin: coins) {
            if (i-coin >= 0 && dp[i-coin] != -1) {
                curr = min(curr, dp[i-coin]);
            }
            if (curr != INF)
                dp[i] = 1 + curr;
        }
    }

    cout << dp[x] << nl;
    return 0;
}