import streamlit as st
import random
from plyer import notification

st.title('OTP Generator')

if st.button('Generate OTP'):
     otp = random.randint(1000,9999)
     st.success(f'OTP Generated:{otp}')
     st.code(otp,language='text')

     notification.notify(
         title='your otp',
         message=f"your otp is: {otp},Don't share otp with anyone" ,
         app_name='elite Games',
         timeout=10
     )