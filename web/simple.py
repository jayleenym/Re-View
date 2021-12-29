import streamlit as st
from transformers import BartTokenizer, TFBartForConditionalGeneration, BartConfig
import tokenizers
from model import run_sum
# from confirm_button_hack import cache_on_button_press

st.title("")

# # https://stackoverflow.com/questions/70274841/streamlit-unhashable-typeerror-when-i-use-st-cache/70275957
# @st.cache(hash_funcs={tokenizers.Tokenizer: lambda _: None, tokenizers.AddedToken: lambda _: None})
def load_model():
    model = TFBartForConditionalGeneration.from_pretrained('facebook/bart-large')
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large')
    return model, tokenizer

#facebook_bas
data_load_state = st.text('모델과 토크나이저를 불러오는 중입니다.....')
model, tokenizer = load_model()
data_load_state.text("업로드 완료!")

st.markdown("---")
st.subheader("답변을 추출할 문단을 넣어주세요.")

context_input = st.text_area(
    "Input Context",
    height=250
)



if context_input:
    st.markdown("-------")

    if st.button("Summarization ON"):
        answer = run_sum(
            model=model,
            tokenizer=tokenizer,
            context=context_input,
            )

        st.write("Answer : ", answer)

