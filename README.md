# Ghostwriter Kant

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
1. [GPT-2 simple model](https://github.com/minimaxir/gpt-2-simple)에 칸트의 '순수이성비판'을 학습시켰습니다.<br>
원활한 데이터 학습을 위해 Google colab을 사용하였습니다.<br>
https://colab.research.google.com/drive/1HYvlny9Djt-K_D057DA6Fhjb-Yb0t8Pr?usp=sharing <br>

2. 해당 모델을 통해 length=300인 글을 추출하였습니다.

```python
import gpt_2_simple as gpt2
import os
import requests

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
...
essay = gpt2.generate(sess,prefix=prefix, length=300, return_as_list=True)[0]
```
## Getting Started 

http://164.90.254.84:5000/ 를 통해 체험하실 수 있습니다.

✅ 영어만 사용가능합니다. <br>
✅ Finetuned Model을 직접 사용하기 때문에 로딩이 **매우** **매우** 오래 걸립니다. <br>
✅ Chrome 사용을 권장합니다<br>
✅ `git clone`을 통한 로컬 구동은 어렵습니다. 용량의 문제로 Finetuned Model을 Github에 업로드하지 않았기 때문입니다.<br>


## Prerequisites
```
Flask==1.1.2
gpt-2-simple==0.7.2
requests==2.25.1
tensorflow==1.15.0
```

## Deployment 

- Docker 
- DigitalOcean
<br>

✅ 높은 용량으로 배포가 불안정합니다. 이로 인해 다중 접속이 어려우니 참고하시길 바랍니다.


## Acknowledgments

* 데이터 학습량이 부족한지, 칸트가 공허한 말을 자주 합니다. <br>하지만 현재로도 이미 버거운 상태이기 때문에, 추가적인 학습를 진행하지 않았습니다.

* 백문이불여일견, 직접 서버에 프로젝트를 올리면서 **효율적인 서버 관리**의 중요성을 알게되었습니다.. 

* 서버가 불안정해서 컨테이너를 주기적으로 restart 해야합니다. 개선 방안을 찾아봐야할 것 같습니다.

* 최신 기술에 대한 안내는 주로 영어로 되어있으므로, 프로그래밍과 더불어 영어도 공부해야겠습니다.

* 텐서플로우를 처음 활용하여 많은 부분 헤맸습니다. 서툴지만 이를 활용하여 제작과 배포를 해냈다는 기쁨을 느끼고, <br>단순히 라이브러리를 익히는 수준이 아니라 수학적으로 접근하며 딥러닝에 대해 심화적으로 공부하고자 합니다.
* 프로젝트 추후 개선점
    - 화면 크기와 브라우저에 따른 호환성 개선
    - 도커 환경 개선
    - 로딩 시 로딩에 대한 안내와 문구 생성(ex. *I'm thinking...Wait a moment.*)


## Thanks To
소프트웨어중심대학 공동해커톤과 해당 과제를 통해 한층 더 개발자로서 발전할 수 있었습니다. <br>
이러한 기회를 주신 커먼컴퓨터와 멘토님들께 진심으로 감사의 인사를 드립니다.