#include <iostream>

using namespace std;

class geek{
  public:
    int id;

  geek(){
    cout << "default constructor " << endl;
    id = -1;
  }

  geek(int a){
    cout << "parameterised constructor " << endl;
    id = a;
  }

  ~geek(){
    cout << "destructor called" << endl;
  }
};

int main(){
  geek p1;
  cout << p1.id << endl;

  geek p2(10);
  cout << p2.id << endl;

  return 0;
}
