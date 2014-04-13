// This is the body of module 'farm' declared in the crate root.

pub fn chicken() { println!("cluck cluck"); }
pub fn cow() { println!("mooo"); }

pub mod barn {
    // Body of module 'barn'

    pub fn hay() { println!("..."); }
}
