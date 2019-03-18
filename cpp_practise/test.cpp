/////////////////////////////////////////////////////////////////////
// Sample program to test C++14 compiler compatibility.
// This program should compile clean in C++14 mode. Use
// either the -std=c++14 or -std=c++1y command-line option
// with a gcc/g++ compiler. Anything since gcc 4.9.2 should
// work fine.
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>
#include <string>

using namespace std;

int i = 100, j = 120, k = 500, m = 1000;
const char *names[] {"this", "is", "a", "test", "zoo", "foo"};
bool compare_shared_ptrs(const shared_ptr<string> &p1, const shared_ptr<string> &p2)
{
    return *p1 < *p2;
}

int main()
{
    vector<shared_ptr<string>> vps;
    for (auto s : names)
        vps.push_back(make_shared<string>(s));
    
    for_each(begin(vps), end(vps),
        []( decltype(*begin(vps))& x ) { cout << *x << ' '; } );
    cout << endl;
    
    for (auto v : vps) { cout << *v << ' '; }
    cout << endl;
    
    sort(begin(vps), end(vps), []( // C++11
    const shared_ptr<string>& p1, const shared_ptr<string>& p2 )
    { return *p1 < *p2; } );
    
    cout << "After sorting:\n";
    for (auto v : vps) { cout << *v << ' '; }
    cout << endl;
    
    sort(begin(vps), end(vps), [] // C++14
        (const auto &p1, const auto &p2) { return *p1 > *p2; });
    cout << "After reverse sorting:\n";
    for (auto v : vps) { cout << *v << ' '; }
    cout << endl;
    
    auto getsize = [](const vector<shared_ptr<string>> &v)
        { return v.size();};
    cout << "getsize(vps) = " << getsize(vps) << endl;
    
    auto getsize2 = []( const auto &c ) { return c.size(); };
    cout << "getsize2(vps) = " << getsize2(vps) << endl;
}
////////////////////////////////////////////////////////////////////