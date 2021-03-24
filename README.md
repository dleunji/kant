# Ghostwriter Kant

![스크린샷 2021-03-24 오전 11 03 03](https://user-images.githubusercontent.com/46207836/112243495-00699c80-8c91-11eb-9da5-b46d10e61593.png)
임마누엘 칸트는 도덕, 이상, 형이상학 등 다양한 주제를 다루는 위대한 철학자압나다.<br>
그의 철학 사상들은 상당히 심오하고 어렵기에 칸트에 관한 과제는 학생들에게 큰 부담입니다.<br>
그래서 칸트는 대필작가로 활동하며 칸트에 관한 에세이를 써야하는 철학과 대학생들을 돕고자 합니다. <br>
에세이의 머리말을 입력하면 칸트가 다음 내용을 작성해줍니다.<br>
예를 들어 위와 같이 'The demon'을 입력하면, 아래와 같이 에세이가 작성됩니다.<br>

![스크린샷 2021-03-24 오전 11 03 41](https://user-images.githubusercontent.com/46207836/112243549-2000c500-8c91-11eb-88cc-2aed2b15a363.png)


## Background
철학과 학생으로서 전공 수업인 '서양근대철학사'에서 칸트의 매운 맛으로 인해 FA를 받은 아픔을 컴퓨터공학적으로 승화하였습니다.<br>
(FA란, 서강대학교만의 출석수 미달로 인한 유급제도입니다.. 당시에 어린 마음에 칸트가 싫어서 도망쳤습니다.🤦‍♀️)<br>
(~~다행히 다음학기에 재수강하여 칸트와 재회의 악수를 나눈 뒤 좋은 성적을 거뒀습니다.~~)<br>

## How to Make
1. GPT-2 simple model에 칸트의 '순수이성비판'을 학습시켜 모델을 생성하였습니다.
2. 해당 모델을 통해 length=300인 글을 추출하였습니다.

```
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
...
essay = gpt2.generate(sess,prefix=prefix, length=300, return_as_list=True)[0]
```
✅ 원활한 데이터 학습을 위해 Google colab을 사용하였습니다.
https://colab.research.google.com/drive/1HYvlny9Djt-K_D057DA6Fhjb-Yb0t8Pr?usp=sharing


## Getting Started 

http://164.90.254.84:5000/ 를 통해 체험하실 수 있습니다.

✅ 영어만 사용가능합니다. <br>
✅ Finetuned Model을 직접 사용하기 때문에 로딩이 **매우** 오래 걸립니다. <br>
✅ Chrom사용을 권장합니다<br>
✅ `git clone`을 통한 로컬 구동은 어렵습니다. 용량의 문제로 Finetuned Model이  Github에 없기 때문입니다.<br>



### Prerequisites / 선행 조건

아래 사항들이 설치가 되어있어야합니다.

```
Flask==1.1.2
gpt-2-simple==0.7.2
requests==2.25.1
tensorflow==1.15.0
```

## Running the tests / 테스트의 실행

어떻게 테스트가 이 시스템에서 돌아가는지에 대한 설명을 합니다

### 테스트는 이런 식으로 동작합니다

왜 이렇게 동작하는지, 설명합니다

```
예시
```

### 테스트는 이런 식으로 작성하시면 됩니다

```
예시
```

## Deployment / 배포

Add additional notes about how to deploy this on a live system / 라이브 시스템을 배포하는 방법

## Built With / 누구랑 만들었나요?

* [이름](링크) - 무엇 무엇을 했어요
* [Name](Link) - Create README.md

## Contributiong / 기여

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us. / [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) 를 읽고 이에 맞추어 pull request 를 해주세요.

## License / 라이센스

This project is licensed under the MIT License - see the [LICENSE.md](https://gist.github.com/PurpleBooth/LICENSE.md) file for details / 이 프로젝트는 MIT 라이센스로 라이센스가 부여되어 있습니다. 자세한 내용은 LICENSE.md 파일을 참고하세요.

## Acknowledgments / 감사의 말

* Hat tip to anyone whose code was used / 코드를 사용한 모든 사용자들에게 팁
* Inspiration / 영감
* etc / 기타