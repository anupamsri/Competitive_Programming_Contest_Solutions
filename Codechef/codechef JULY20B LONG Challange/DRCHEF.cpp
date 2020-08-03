#include <bits/stdc++.h>
#define ll long long int
using namespace std;


int main(){
    int t; cin >> t;
    while(t--)
        {
    ll NN11, xx111, dinmensdays = 0;
    cin >> NN11 >> xx111;
    vector<ll> aa111(NN11);
    for(int i111=0; i111<NN11; i111++){
        cin >> aa111[i111];
    }

    sort(aa111.begin(), aa111.end());
    vector<ll>::iterator it = lower_bound(aa111.begin(), aa111.end(), xx111);
    ll lambab = it - aa111.begin();

    for(int i111=lambab; i111<NN11; i111++)
    {
        if(xx111<aa111[i111])
        {
            while(xx111<aa111[i111])
            {
                xx111 = 2*xx111;
                dinmensdays++;
            }
            dinmensdays++;
        }
        else
        dinmensdays++;
        xx111 = 2*aa111[i111];
    }
        ll totalsis = lambab + dinmensdays;
        if(lambab != 0)
        {
            dinmensdays = 0;
            lambab--;
            for(int i111=lambab; i111<NN11; i111++)
            {
                if(xx111 < aa111[i111])
                {
                    while(xx111<aa111[i111])
                    {
                        xx111 = 2*xx111;
                        dinmensdays++;
                    }
                    dinmensdays++;
                }
                else
                dinmensdays++;
                xx111 = 2*aa111[i111];
            }
            if(dinmensdays+lambab<totalsis)
                cout << dinmensdays+lambab << endl;
            else
                cout << totalsis << endl;
        }
        else
            cout << totalsis << endl;
}
    return 0;
}