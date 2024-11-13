""

'''
use pyo3::prelude::*;

#[pyfunction]
fn greet(name: &str) -> String {
	format!("Hello, {}!", name)
}

#[pymodule]
fn mymodule(py: Python, m: &PyModule) -> PyResult<()> {
	m.add_function(wrap_pyfunction!(greet, m)?)?;
	Ok(())
}



'''