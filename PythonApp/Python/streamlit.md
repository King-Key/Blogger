- stream.progress()  //实时显示进度状态

  ```python
  import streamlit as st
  import time
  
  latest_iteration=st.empty()
  bar=st.progress(0)
  
  for i in range(100):
  	latest_iteration.text("iteration {i+1}")
  	bar.progress(i+1)
  	time.sleep(0.1)
  ```

  

