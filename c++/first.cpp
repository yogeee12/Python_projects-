#include <iostream>
#include <string>
using namespace std;

string even_odd(int num){
    if (num%2 == 0){
        return "Even\n";
    }
    else{
        return "odd\n";
    }
}
int main() {
    cout<<even_odd(6);
}