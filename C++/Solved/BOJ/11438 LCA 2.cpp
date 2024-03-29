#include <bits/stdc++.h>
using namespace std;
// 11438 LCA 2

const int MAXN = 100002;
const int root = 1;
int N, M;
vector<int> anc[MAXN];
vector<int> adj[MAXN];
int depth[MAXN];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N;
  for (int i = 0; i < N - 1; i++) {
    int a, b;
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }
  queue<int> Q({root});
  depth[root] = 0;
  // build anc array
  while (!Q.empty()) {
    int par = Q.front();
    Q.pop();
    for (auto c : adj[par]) {
      // if selected child is root
      if (c == root) continue;
      // if selected child was visited
      if (anc[c].size()) continue;
      depth[c] = depth[par] + 1;
      anc[c].push_back({par});
      int idx = 0;
      while (1) {
        // 2^(idx+1)-st ancestor = 2^(idx)-st ancestor(=bridge)'s 2^(idx)-st ancestor
        int bridge = anc[c].back();
        if (anc[bridge].size() <= idx) break;
        anc[c].push_back(anc[bridge][idx]);
        idx++;
      }
      Q.push(c);
    }
  }
  cin >> M;
  for (int qqq = 0; qqq < M; qqq++) {
    int a, b;
    cin >> a >> b;
    // depth equalization
    if (depth[a] < depth[b]) swap(a, b);
    while (depth[a] != depth[b]) {
      // start from farmost ancestor
      for (int i = anc[a].size() - 1; - 1 < i; i--) {
        if (depth[anc[a][i]] < depth[b]) continue;
        a = anc[a][i];
        break;
      }
    }
    // find LCA
    if (a == b) {
      cout << a << '\n';
      continue;
    }
    while (anc[a][0] != anc[b][0]) {
      for (int i = anc[a].size() - 1; - 1 < i; i--) {
        if (anc[a][i] == anc[b][i]) continue;
        a = anc[a][i];
        b = anc[b][i];
        break;
      }
    }
    cout << anc[a][0] << '\n';
  }
}