class matrix {
public:
    vector<vector<int>> m;
    matrix(int n = 0): m(n, vector<int>(n)) {}
    vector<int>& operator [] (int i) { return m[i]; }
    matrix& operator += (matrix m) { return *this = *this + m; }
    matrix& operator *= (matrix m) { return *this = *this * m; }

    friend matrix operator + (matrix a, matrix b) {
        int n = a.m.size();
        matrix ret(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ret[i][j] = (a[i][j] + b[i][j]) % mod;
            }
        }
        return ret;
    }

    friend matrix operator * (matrix a, matrix b) {
        int n = a.m.size();
        matrix ret(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    ret[i][j] += a[i][k] * b[k][j];
                    ret[i][j] %= mod;
                }
            }
        }
        return ret;
    }
};
