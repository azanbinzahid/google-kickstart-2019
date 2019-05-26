  #include <iostream>
  #include <math.h>
  #include <string>

  using namespace std;
  
  bool digit(int n, int k)
  {
      string s = to_string(n);
      for(int i = 0; i < s.length(); i++){
          if (s[i]=='4') return 1;
      }
      return 0;
 }

int main(){

int T;
cin>>T;
for (int t = 0; t<T; t++){
    int N, A, B;
    cin >> N;
    int cc = 1;
    while(1){
        int a, b, n;
        bool checka, checkb = 0;
        cc++;
        n = N/cc;
        cout<<n<<endl;
        a = n; 
        b = N - a;
        
        checka = digit(a, 4);
        checka = digit(b, 4);


        if (a+b == N){
            if (checka || checkb) continue;
            A = a;
            B = b;
            break;
        }

        a = a+1 ;
        b = N-a;

        checka = digit(a, 4);
        checka = digit(b, 4);


        if (a+b == N){
            if (checka || checkb) continue;
            A = a;
            B = b;
            break;
        }
        }
        cout<<"Case #"<<t+1<<": "<<A<<" "<<B<<"\n";
    }
}