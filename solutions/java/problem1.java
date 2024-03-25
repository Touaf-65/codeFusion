import java.math.BigInteger;


public final class p387 {
	
	public static void main(String[] args) {
		System.out.println(new p387().run());
	}
	
	
	private static final long LIMIT = 100000000000000L;
	
	
	private BigInteger sum = BigInteger.ZERO;
	
	public String run() {
		for (int i = 1; i <= 9; i++)  // Tous les nombres à un chiffre sont trivialement des nombres Harshad
			findHarshadPrimes(i, i, false);
		return sum.toString();
	}
	
	
	// Remarque : n doit être un nombre Harshad tronquable à droite et les autres arguments sont des propriétés du nombre n.
	private void findHarshadPrimes(long n, int digitSum, boolean isStrong) {
		// Décaler d'un chiffre vers la gauche et essayer les 10 possibilités pour le chiffre le plus à droite
		long m = n * 10;
		int s = digitSum;
		for (int i = 0; i < 10 && m < LIMIT; i++, m++, s++) {
			if (isStrong && isPrime(m))
				sum = sum.add(BigInteger.valueOf(m));
			if (m % s == 0)
				findHarshadPrimes(m, s, isPrime(m / s));
		}
	}
	
	
	private static boolean isPrime(long x) {
		if (x < 0)
			throw new IllegalArgumentException("Negative number");
		if (x == 0 || x == 1)
			return false;
		for (long i = 2, end = Library.sqrt(x); i <= end; i++) {
			if (x % i == 0)
				return false;
		}
		return true;
	}
	
}
