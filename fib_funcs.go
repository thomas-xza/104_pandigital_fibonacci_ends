//  ---------------------------------------------------------------------------------
//  ---------------------------------------------------------------------------------

//  THIS IS THE CHECKED, RECOMMENTED, EDITED VERSION OF THE OUTPUT OF GPT-OSS WHEN
//  REQUESTING A GO PORT OF fib_funcs.py

//  MINIMAL EDITS WERE MADE; THE PORT SEEMS LARGELY SIMILAR, SANE AND LOGICAL.

//  ---------------------------------------------------------------------------------
//  ---------------------------------------------------------------------------------


package main


import (
	"fmt"
	"math/big"
)


func main() {

     fmt.Println("main()")
  
	//  Allocate memory for large integer, via binary left shifting.
  
	limit := new(big.Int).Lsh(big.NewInt(1), 128)
  
	findPandigitals(limit)
  
}


func findPandigitals(limit *big.Int) {
  
	found := false
  
  //  Initialise Fibonacci sequence.
  
	f1 := big.NewInt(1)
	f2 := big.NewInt(1)
  
	k := big.NewInt(2)

	for !found && k.Cmp(limit) < 0 {

    //  Generate next Fibonacci number and increment k of F_k.

		k.Add(k, big.NewInt(1))
  
		f1, f2 = f2, new(big.Int).Add(f1, f2)

    //  Extract the two sets from the Fibonacci number.

		fibStr := f2.String()

		first9, last9 := splitDigits(fibStr)

    //  Check the sets.
    
		res := checkFN(first9, last9)

		if res[0] || res[1] {
      
			// fmt.Printf("%d %v\n", k, res, fibStr)
      
			fmt.Printf("%d %v\n", k, res)
      
		}
    
	}
  
}


func splitDigits(s string) ([]int, []int) {

  //  Go does not have any native string-to-integer-set conversion, perhaps.
  
	toInts := func(sub string) []int {

    //  Allocate a variate the length of the string.
    
		out := make([]int, len(sub))

    //  Iterate over each character and convert from ASCII to binary.
    
		for i, ch := range sub {
      
			out[i] = int(ch - '0')
      
		}
    
		return out
    
	}

  //  If length of string below or equal to 9, return verbatim output after conversion.

	if len(s) <= 9 {
		return toInts(s), toInts(s)
	}

  //  Else return first and last sets of 9.
  
	return toInts(s[:9]), toInts(s[len(s)-9:])
  
}


func checkFN(first, last []int) [2]bool {

  //  Succinct calling pandigital check twice and returning of slice of booleans.
  
	return [2]bool{
		isPandigital(first),
		isPandigital(last),
	}
  
}

func isPandigital(digits []int) bool {

  //  If length too short, definitely not pandigital.
  
	if len(digits) != 9 {
		return false
	}

  //  This port uses true and false instead of counters.
  
	seen := [10]bool{}

  //  Iterate over the digits of the 9-integer set.
  
	for _, d := range digits {

    //  If the digit is a 0, set cannot bet pandigital.
    
		if d == 0 {
			return false
		}

    //  If the digit has already appeared in set, cannot be pandigital.
    
		if seen[d] {
			return false
		}

    //  Else mark digit as having occurred once.
    
		seen[d] = true
	}

  //  Double-check that all digits 1-9 occurred once each.

	for i := 1; i <= 9; i++ {
    
		if !seen[i] {
			return false
		}
    
	}
  
	return true
  
}
