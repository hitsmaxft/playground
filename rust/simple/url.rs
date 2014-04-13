use std::result::Result;
use std::libc;

pub enum ErrorCode {
    EINVAL = libc::EINVAL as int,
}

pub fn parse_uri<'r>(uri: &'r str) -> Result<(&'r str, &'r str), ErrorCode> {
    match uri.find_str("://") {
        Some(pos) => {
            let protocol = uri.slice_to(pos);
            let address = uri.slice_from(pos + 3);
            if protocol.len() == 0 || address.len() == 0 {
                Err(EINVAL)
            } else {
                Ok((protocol, address))
            }
        },
        None => Err(EINVAL),
    }
}

fn main() {
    match parse_uri("http://s.taobao.com") {
        Ok((scheme, uri)) => {
            println!("scheme is {}, uri is {}", scheme, uri)
        },
        Err(_) => {println!("error");},
    }
}
