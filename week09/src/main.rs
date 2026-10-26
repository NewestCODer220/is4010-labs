// Week 09: Rust basics
//
// Implement each function below so that the tests at the bottom of this file pass.
// Run your tests with: cargo test
//
// Rules:
//   - Replace every `todo!()` with a real implementation.
//   - Do NOT modify the test module.
//   - Your code must compile with zero Clippy warnings (cargo clippy -- -D warnings).

fn main() {
    println!("Week 09: Rust basics");

    // Feel free to call your functions here to try them out.
    println!("add(3, 4) = {}", add(3, 4));
    println!("multiply(3, 4) = {}", multiply(3, 4));
    println!("is_even(7) = {}", is_even(7));
    println!("max(3, 9) = {}", max(3, 9));
    println!("square(5) = {}", square(5));
    println!("reverse_string(\"hello\") = {}", reverse_string("hello"));
    println!(
        "find_max_in_vec(&[1, 5, 3]) = {:?}",
        find_max_in_vec(&[1, 5, 3])
    );
    println!(
        "count_evens(&[1, 2, 3, 4]) = {}",
        count_evens(&[1, 2, 3, 4])
    );
    println!(
        "concat_with_separator(&[\"hello\", \"world\"], \"-\") = {}",
        concat_with_separator(&["hello", "world"], "-")
    );
}
// ============================================================================
// PART 1: Basic arithmetic
// ============================================================================

pub fn add(a: i32, b: i32) -> i32 {
    // No semicolon on the final line creates an implicit return
    a + b
}

pub fn multiply(a: i32, b: i32) -> i32 {
    a * b
}

// ============================================================================
// PART 2: Boolean logic
// ============================================================================

pub fn is_even(n: i32) -> bool {
    // Returns true if the remainder of division by 2 is exactly 0
    n % 2 == 0
}

// ============================================================================
// PART 3: Comparisons
// ============================================================================

pub fn max(a: i32, b: i32) -> i32 {
    // Rust's standard library provides a built-in max method for integers
    a.max(b)
}

// ============================================================================
// PART 4: Expressions
// ============================================================================

pub fn square(n: i32) -> i32 {
    n * n
}

// ============================================================================
// PART 5: String operations
// ============================================================================

pub fn reverse_string(s: &str) -> String {
    // chars() breaks the string into an iterator of characters
    // rev() reverses the order
    // collect() gathers them back into a new String
    s.chars().rev().collect()
}

pub fn concat_with_separator(words: &[&str], sep: &str) -> String {
    // Slices have a built-in join method that perfectly handles this
    words.join(sep)
}

// ============================================================================
// PART 6: Collections and Option
// ============================================================================

pub fn find_max_in_vec(numbers: &[i32]) -> Option<i32> {
    // iter() creates an iterator over references (&i32)
    // copied() converts those references into actual values (i32)
    // max() finds the highest value, automatically returning Option::None if empty
    numbers.iter().copied().max()
}

pub fn count_evens(numbers: &[i32]) -> usize {
    // filter() keeps only the items where the closure condition is true
    // count() tallies how many items made it through the filter
    numbers.iter().filter(|&&x| x % 2 == 0).count()
}

// ============================================================================
// TESTS: DO NOT MODIFY
// ============================================================================
#[cfg(test)]
mod tests {
    use super::*;

    // --- add ---
    #[test]
    fn test_add_positive() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    fn test_add_with_zero() {
        assert_eq!(add(0, 7), 7);
        assert_eq!(add(7, 0), 7);
    }

    #[test]
    fn test_add_negative() {
        assert_eq!(add(-1, 1), 0);
        assert_eq!(add(-3, -4), -7);
    }

    // --- multiply ---
    #[test]
    fn test_multiply_positive() {
        assert_eq!(multiply(3, 4), 12);
    }

    #[test]
    fn test_multiply_by_zero() {
        assert_eq!(multiply(0, 99), 0);
        assert_eq!(multiply(42, 0), 0);
    }

    #[test]
    fn test_multiply_negative() {
        assert_eq!(multiply(-2, 5), -10);
        assert_eq!(multiply(-3, -3), 9);
    }

    // --- is_even ---
    #[test]
    fn test_is_even_true() {
        assert!(is_even(0));
        assert!(is_even(2));
        assert!(is_even(100));
    }

    #[test]
    fn test_is_even_false() {
        assert!(!is_even(1));
        assert!(!is_even(7));
        assert!(!is_even(99));
    }

    #[test]
    fn test_is_even_negative() {
        assert!(is_even(-4));
        assert!(!is_even(-3));
    }

    // --- max ---
    #[test]
    fn test_max_first_larger() {
        assert_eq!(max(9, 3), 9);
    }

    #[test]
    fn test_max_second_larger() {
        assert_eq!(max(3, 9), 9);
    }

    #[test]
    fn test_max_equal() {
        assert_eq!(max(5, 5), 5);
    }

    #[test]
    fn test_max_negative() {
        assert_eq!(max(-1, -5), -1);
    }

    // --- square ---
    #[test]
    fn test_square_positive() {
        assert_eq!(square(5), 25);
        assert_eq!(square(1), 1);
    }

    #[test]
    fn test_square_zero() {
        assert_eq!(square(0), 0);
    }

    #[test]
    fn test_square_negative() {
        // (-3)² = 9
        assert_eq!(square(-3), 9);
    }

    // --- reverse_string ---
    #[test]
    fn test_reverse_string_basic() {
        assert_eq!(reverse_string("hello"), "olleh");
        assert_eq!(reverse_string("rust"), "tsur");
    }

    #[test]
    fn test_reverse_string_empty() {
        assert_eq!(reverse_string(""), "");
    }

    #[test]
    fn test_reverse_string_single_char() {
        assert_eq!(reverse_string("a"), "a");
    }

    // --- concat_with_separator ---
    #[test]
    fn test_concat_basic() {
        assert_eq!(
            concat_with_separator(&["hello", "world"], "-"),
            "hello-world"
        );
        assert_eq!(concat_with_separator(&["a", "b", "c"], ","), "a,b,c");
    }

    #[test]
    fn test_concat_empty() {
        assert_eq!(concat_with_separator(&[], ","), "");
    }

    #[test]
    fn test_concat_single_word() {
        assert_eq!(concat_with_separator(&["hello"], "-"), "hello");
    }

    // --- find_max_in_vec ---
    #[test]
    fn test_find_max_basic() {
        assert_eq!(find_max_in_vec(&[1, 5, 3]), Some(5));
        assert_eq!(find_max_in_vec(&[10, 2, 8, 4]), Some(10));
    }

    #[test]
    fn test_find_max_empty() {
        assert_eq!(find_max_in_vec(&[]), None);
    }

    #[test]
    fn test_find_max_negative() {
        assert_eq!(find_max_in_vec(&[-5, -1, -10]), Some(-1));
    }

    #[test]
    fn test_find_max_single() {
        assert_eq!(find_max_in_vec(&[42]), Some(42));
    }

    // --- count_evens ---
    #[test]
    fn test_count_evens_mixed() {
        assert_eq!(count_evens(&[1, 2, 3, 4]), 2);
        assert_eq!(count_evens(&[2, 4, 6]), 3);
    }

    #[test]
    fn test_count_evens_none() {
        assert_eq!(count_evens(&[1, 3, 5]), 0);
    }

    #[test]
    fn test_count_evens_empty() {
        assert_eq!(count_evens(&[]), 0);
    }

    #[test]
    fn test_count_evens_negative() {
        assert_eq!(count_evens(&[-2, -1, 0, 1, 2]), 3); // -2, 0, 2 are even
    }
}
