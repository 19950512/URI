import 'dart:io';

void main() {
  int N = int.parse(stdin.readLineSync() ?? "");
  print((((N + 1) * (N + 2)) / 2).round());
}
