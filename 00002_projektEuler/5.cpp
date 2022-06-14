//
//  main.cpp
//  pointers
//
//  Created by Nishant Patil on 4/12/19.
//  Copyright © 2019 Nishant Patil. All rights reserved.
//

#include <iostream>

using namespace std;

int checkdiv(int num){
    for (int i = 1; i < 20; i++){
        if (num % i != 0){
            return false;
        }
    }
    return num;
}

int main(int argc, const char * argv[]) {
    int check = 1;
    
    cout << "running nums" << endl;
    while(true){
        if (checkdiv(check)){
            cout << "found number = " << check << endl;
            break;
        }
        check = check + 1;
    }
    
    cout << "finished" << endl;
    
    return 0;
}
