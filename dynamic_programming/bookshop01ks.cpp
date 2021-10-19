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
#define print2(a, m, n) for(int i=0;i<m;++i){for(int j=0;j<n;++j)\
{cout<<a[i][j]<<' ';}cout<<nl;}

///////////////////////////////////////////////////////////////////////////////

/*
You are in a book shop which sells n different books. You know the price and 
number of pages of each book.

You have decided that the total price of your purchases will be at most x. 
What is the maximum number of pages you can buy? You can buy each book at most 
once.

Input
The first input line contains two integers n and x: the number of books and 
the maximum total price.
The next line contains n integers h1,h2,…,hn: the price of each book.
The last line contains n integers s1,s2,…,sn: the number of pages of each book.

Output
Print one integer: the maximum number of pages.

Constraints
    1<=n<=1000
    1<=x<=105
    1<=h_i,s_i<=1000

Example
    Input:
    4 10
    4 8 5 3
    5 12 8 1

    Output:
    13

Explanation: You can buy books 1 and 3. Their price is 4+5=9 and the number of pages is 5+8=13.
*/

const int MAXM = 1000;
const int MAXN = 1e5;
ll dp[MAXN+1] = {0};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    /*
    Standard 0-1 knapsack problem
    Given some subset of 1,...,n, require that sum(h_i) <= x, such that
    sum(s_i) is maximized.
    */

    int n, x; cin >> n >> x;
    vector<int> h(n); // prices
    vector<int> s(n); // number of pages
    for (int i = 0; i < n; ++i) {
        cin >> h[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }
    
    fill(dp+1, dp+x+1, -1);

    for (int i = 0; i < n; ++i) {
        // 
        for (int j = x-h[i]; j >= 0; --j) {
            if (dp[j] != -1)
                dp[j+h[i]] = max(dp[j+h[i]], dp[j]+s[i]);
        }
    }

    for (int i = 1; i <= x; ++i) {
        dp[i] = max(dp[i], dp[i-1]);
    }
    
    cout << dp[x] << nl;
    return 0;
}