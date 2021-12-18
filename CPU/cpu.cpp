#include <iostream>
#include <math.h>
#include <time.h>
#include <omp.h>


using namespace std;
bool czy_pierwsza(int liczba){
    for(long long i=2; i<=sqrt(liczba); i++){
        if(liczba%i==0){
            return false;
        }
    }
    return true;
}

long long policzPierwsze(int a, int b){
    long long pierwsze = 0;
    #pragma omp parallel for reduction(+:pierwsze)
        for(long long i=a;i<=b;i++){
            if (czy_pierwsza(i)){
                pierwsze++;
            }
        }
    return pierwsze;
}
int main(int argc, char const *argv[])
{
    double itime, ftime, exec_time;
    int a = 10;
    int b = 2000000;
    
    itime = omp_get_wtime();
    cout<<"Ilość liczb pierwszych w przedziale od "<<a<<" do "<<b<<" wynosi: "<<policzPierwsze(a, b)<<endl;
    ftime = omp_get_wtime();
    exec_time = ftime - itime;
    cout<<"Elapsed time: "<<exec_time<<" s"<<endl;
    return 0;
}