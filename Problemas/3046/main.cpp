#include <iostream>

int main() {
    int N;
    int x;

    std::cin >> N;

    x = ((N+1)*(N+2))/2;

    std::cout << std::to_string(x) + "\n";
    return 0;
}