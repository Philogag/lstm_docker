import jieba
import numpy as np
from gensim.models.word2vec import Word2Vec
from gensim.corpora.dictionary import Dictionary
from keras.preprocessing import sequence
import sys
import yaml
from keras.models import model_from_yaml
from copy import deepcopy

maxlen = 100
print("loading lstm model...")
with open('./model/lstm.yml', 'r') as f:
    yaml_string = yaml.load(f)
lstm_model = model_from_yaml(yaml_string)

print('loading model weights...')
lstm_model.load_weights('./model/lstm.h5')
lstm_model.compile(loss='categorical_crossentropy',
            optimizer='adam', metrics=['accuracy'])

print("loading word split model...")
w2v_model = Word2Vec.load('./model/Word2vec_model.pkl')
gensim_dict = Dictionary()
gensim_dict.doc2bow(w2v_model.wv.vocab.keys(),
                    allow_update=True)

def _create_dictionaries(combined):
    w2v_model.clear_sims()
    if (combined is not None) and (w2v_model is not None):
        gensim_dict = Dictionary()
        gensim_dict.doc2bow(w2v_model.wv.vocab.keys(),
                            allow_update=True)
        #  freqxiao10->0 所以k+1
        w2indx = {v: k + 1 for k, v in gensim_dict.items()}  # 所有频数超过10的词语的索引,(k->v)=>(v->k)
        w2vec = {word: w2v_model[word] for word in w2indx.keys()}  # ����Ƶ������10�Ĵ���Ĵ�����, (word->model(word))

        def parse_dataset(combined):  # �հ�-->��ʱʹ��
            """Words become integers."""
            data = []
            for sentence in combined:
                new_txt = []
                for word in sentence:
                    try:
                        new_txt.append(w2indx[word])
                    except:
                        new_txt.append(0)  # freqxiao10->0
                data.append(new_txt)
            return data  # word=>index

        combined = parse_dataset(combined)
        combined = sequence.pad_sequences(combined, maxlen=maxlen)  # 每个句子所含词语对应的索引，所以句子中含有频数小于10的词语，索引为0
        return w2indx, w2vec, combined

def _input_transform(string):
    words = jieba.lcut(string)
    words = np.array(words).reshape(1, -1)
    _, _, combined = _create_dictionaries(words)
    return combined

def predict(string):
    data = _input_transform(string)
    data.reshape(1, -1)
    # print(data)
    result = lstm_model.predict_classes(data)
    return int(result[0])


if __name__ == "__main__":
    # print(LSTM().predict("真的一般，没什么可以学习的"))
    print(predict("不好"))
    print(predict("好"))
    print(predict("不错"))
    