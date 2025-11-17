#include <iostream>
using namespace std;
//#define md long long int;
int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        long long int a, b;
        cin >> a >> b;
        long long int e1, e2, o1, o2;

        e1 = a / 2;
        if (a % 2 == 0)
        {
            o1 = e1;
        }
        else
        {
            o1 = e1 + 1;
        }

        e2 = b / 2;
        if (b % 2 == 0)
        {
            o2 = e2;
        }
        else
        {
            o2 = e2 + 1;
        }

        //cout<<"for a no_of_even="<<e1<<" and no of odd="<<o1<<endl;
        //  cout<<"for b no_of_even="<<e2<<" and no of odd="<<o2<<endl;
        cout << (e1 * e2 + o1 * o2) << endl;
    }
    return 0;
}