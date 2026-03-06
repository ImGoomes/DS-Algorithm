#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int *data;
  int size;
  int capacity;
} Array;


int main() {

}

int next_power_of_2(int n) {
  int cap = 16;

  while (cap < n){
    cap = cap * 2;
  }
  return cap;
}

Array *array_new(int inital_capacity){
  Array *arr = (Array *)malloc(sizeof(Array));
  arr->capacity = next_power_of_2(inital_capacity);
  arr->data = (int *)malloc(arr->capacity * sizeof(int));
  arr->size = 0;
  return arr;
}
