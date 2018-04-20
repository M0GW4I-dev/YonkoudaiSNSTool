## YonkoudaiSNSTool

このツールを用いた損害について私は一切責任を持ちません

### Example
```python3
#Example.py

import req
#username:foo password:bar000 fullname:nick hogehoge@test.co.jp
def main():
	r = req.gen_account("foo","nick","bar000","hogehoe")
	assert r.status_code==200, "Failed"
	#Tweet content is Tweet
	r = req.tweet("foo","bar000","Tweet")
	assert r.status_code==200, "Tweet failed"

if __name__=='__main__':
	main()
```
* Execution
```
%python3 Example.py
```

	
