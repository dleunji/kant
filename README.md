# Ghostwriter Kant
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize-kant-dleunji.endpoint.ainize.ai)<br>

![스크린샷 2021-03-24 오전 11 03 03](https://user-images.githubusercontent.com/46207836/112243495-00699c80-8c91-11eb-9da5-b46d10e61593.png)
[임마누엘 칸트](https://ko.wikipedia.org/wiki/임마누엘_칸트)는 도덕, 이상, 형이상학 등 다양한 주제를 다루는 위대한 철학자압나다.<br>
그의 철학 사상들은 상당히 심오하고 어렵기에 칸트에 관한 과제는 학생들에게 큰 부담입니다.<br>
그래서 칸트는 대필작가로 활동하며 칸트에 관한 에세이를 써야하는 철학과 대학생들을 돕고자 합니다. <br>
에세이의 머리말을 입력하면 칸트가 다음 내용을 작성해줍니다.<br>
예를 들어 위와 같이 'The demon'을 입력하면, 아래와 같이 에세이가 'The demon'을 시작으로 글이 작성됩니다.<br>

![스크린샷 2021-03-24 오전 11 03 41](https://user-images.githubusercontent.com/46207836/112243549-2000c500-8c91-11eb-88cc-2aed2b15a363.png)


## Background
철학 전공 수업인 '서양근대철학사'에서 칸트의 사상이 너무 어려워 굉장히 낮은 성적을 받았습니다...<br>
그 때 상상하기만 했던 프로그램을 직접 구현해보며 아픔을 컴퓨터공학적으로 승화하였습니다.<br>
(여담이지만, 다행히 다음학기에 재수강하여 칸트와 재회의 악수를 나눈 뒤 좋은 성적을 거뒀습니다🙍‍♀️)<br>
<br>

## How to Make
1. 칸트의 순수이성비판을 전처리하여 불필요한 기호와 문자들을 제거하였습니다.
 https://colab.research.google.com/drive/1jhSklYNs17FF5GvlLKs7JCjzkBDbfBrq?usp=sharing
```
 § 5. Metaphysical Exposition of this Conception.

 § 6. Transcendental Exposition of the Conception of Time.

 § 7. Conclusions from the above Conceptions.

 § 8. Elucidation.

 § 9. General Remarks on Transcendental Æsthetic.

 § 10. Conclusion of the Transcendental Æsthetic.
```
```
                      NOTHING
                        AS

                        1
                As Empty Conception
                 without object,
                  _ens rationis_
           2                               3
     Empty object of               Empty intuition
      a conception,                without object,
     _nihil privativum              ens imaginarium_
                        4
                   Empty object
                 without conception,
                  _nihil negativum_
                  
```

2. 전처리된 파일 하나만으로 Teachable NLP를 활용하여 편리하게 GPT-2모델을 Finetuing하였습니다.<br>
Model_url = https://train-avgw7n5kbmsb7wrip2a8-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/gpt-2-en-small-finetune

2. 해당 모델에 prefix를 `form-data` 형식의 request를 보내면, response로 다음 내용이 이어집니다.<br>

## e.g. 
### REQUEST
```JSON
{
    "context" : "The demon"
}
```
### RESPONSE


```JSON
{
    "text": "The demon is merely an appearance, and never a thing that is absolutely\nin itself necessary. If I make abstraction of the relation of\nphenomena in space (as in the representation of a body), there can exist no\nthing that is absolutely necessary. But the mere fact of an existence\nwhich is absolutely necessary is not to be found in any perception\nitself, or in any intuition corresponding to it, except in so far\nas the existence of that which is immediately presupposed in the perception\nis itself the immediate consequence of some other existence. Now as this\ndetermination of the existence of things is possible only under the\npresupposition of a given existence (for example, that the body has\nlength that is possible only by means of a straight line), the existence\nof the thing which is immediately presupposed to be necessary is a proposition\nwhich requires deeper insight into the subject than the mere conception of\na thing in itself. Now this is all well and good,"
}
```

## Deployment 
- Docker 
- Ainize
<br>

## Acknowledgments

* 데이터 학습량이 부족한지, 칸트가 공허한 말을 자주 합니다. <br> 하지만 현재로도 이미 버거운 상태이기 때문에, 추가적인 학습를 진행하지 않았습니다.

* 백문이불여일견, 직접 서버에 프로젝트를 올리면서 **효율적인 서버 관리**의 중요성을 알게되었습니다.. 

* 최신 기술에 대한 안내는 주로 영어로 되어있으므로, 프로그래밍과 더불어 영어도 공부해야겠습니다.

* 텐서플로우를 처음 활용하여 많은 부분 헤맸습니다. 서툴지만 이를 활용하여 제작과 배포를 해냈다는 기쁨을 느끼고, <br>단순히 라이브러리를 익히는 수준이 아니라 수학적으로 접근하며 딥러닝에 대해 심화적으로 공부하고자 합니다.
* 프로젝트 추후 개선점
    - 화면 크기와 브라우저에 따른 호환성 개선 <br> 
    버튼 위치 개선
    - 도커 환경 개선<br>
    - 로딩 시 로딩에 대한 안내와 문구 생성(ex. *I'm thinking...Wait a moment.*)<br>


## Thanks To
소프트웨어중심대학 공동해커톤과 해당 과제를 통해 한층 더 개발자로서 발전할 수 있었습니다. <br>
이러한 기회를 주신 커먼컴퓨터와 멘토님들께 진심으로 감사의 인사를 드립니다.

## 2021.04.05 개선 일지
1. Ainize를 통해 배포함으로써 GPU를 통해 배포안정성과 속도가 급격히 개선되었습니다.(약 6초)

2. 이외에도 체감되는 지연 시간을 줄이기 위해 로딩 바를 생성하였습니다. 내용과 적절히 어울리는 "I'm thinking "문구를 곁들여 프로그램과 어울리도록 하였습니다.

3. 기존의 모델에 불필요한 텍스트가 섞여 있었습니다. 이를 개선하기 위해 파이썬을 통해 텍스트파일을 전처리한 후, 재학습하였습니다.

## 2021.04.14 개선 일지
1. Teachable NLP로 모델이 만들어진 후 자동적으로 서버에 업로드 됨으로써 간편하게 모델을 활용할 수 있습니다.

2. 해당 모델을 활용하여 [TabTab](https://kubecon-tabtab-ainize-team.endpoint.ainize.ai/?modelUrl=https://train-avgw7n5kbmsb7wrip2a8-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/gpt-2-en-small-finetune)에서도 체험이 가능합니다.




