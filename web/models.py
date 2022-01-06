
"""
def run_sum(model, tokenizer, context):
    inputs = tokenizer([context], max_length=1024, return_tensors='tf')
    summary_ids = model.generate(inputs['input_ids'],
                                 num_beams=20, max_length=30, early_stopping=True)
    outputs = [tokenizer.decode(g, skip_special_tokens=True, 
                            clean_up_tokenization_spaces=False) for g in summary_ids]
    
    return outputs
"""
# 군집화
def classification(model, tokenizer):
    input = tokenizer()

# 유용성 점수
# def kobert():
