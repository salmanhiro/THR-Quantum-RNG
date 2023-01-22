import qrng
import streamlit as st

if 'thr' not in st.session_state:
    st.session_state.thr = 0

def on_click_generate_number():
    result = qrng.get_random_double(0,1)
    thr_amount = filter_result(result)
    st.session_state.thr = thr_amount

def filter_result(value):
    if value < 0.5:
        return 1000
    elif value < 0.7:
        return 2000
    elif value < 0.9:
        return 5000
    elif value < 0.99:
        return 10000
    else:
        return 50000

def object_main():
    qrng.set_provider_as_IBMQ('')
    qrng.set_backend()

    st.title("Angpao Generator")
    st.image('angpao.jpg', caption="Image by Jason Leung at Unsplash", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


    st.write("Apps to generate random number of angpao in IDR based on quantum random number")
    st.write("Disclaimer: angpao given by user; salman isn't responsible for any angpao")

    st.button('Click here', on_click=on_click_generate_number)
    st.write('Nice you get ', st.session_state.thr)
    st.write("新年快樂")


if __name__ == '__main__':
    object_main()
