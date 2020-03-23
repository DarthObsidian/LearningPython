template<int i>
struct D {
   D(void*);
   operator int();
};

template<int p, int i>
struct is_prime {
   enum { prim = (p%i) && is_prime
