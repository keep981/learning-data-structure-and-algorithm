#include<iostream>
using namespace std;

bool doseProduceEnough(int d1,int v1,int d2,int v2,int p, int current_days);
int howMuchProduceInGivenDays(int d,int v,int given_days);

int main(){

    int s=1,e=1000000;
    int d1,v1,d2,v2,p;
    cin>>d1>>v1>>d2>>v2>>p;

    int min_days_required;
    while(s<=e){
        int mid=(s+e)/2;
        if(doseProduceEnough(d1,v1,d2,v2,p,mid)){
            min_days_required=mid;
            e=mid-1;
        }
        else{
            s=mid+1;
        }

    }

    cout<<min_days_required<<endl;
    return 0;
}


bool doseProduceEnough(int d1,int v1,int d2,int v2,int p, int current_days){
    int first=howMuchProduceInGivenDays(d1,v1,current_days);
    int second=howMuchProduceInGivenDays(d2,v2,current_days);
    if(first+second >= p)
        return true;
    else
        return false;
}

int howMuchProduceInGivenDays(int d,int v,int given_days){
    int productive_days=given_days-d+1;
    if(productive_days>0)
        return productive_days*v;
    else
        return 0;
}