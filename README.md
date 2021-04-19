# KinD-Net_modify
<br>

해당 코드는 저조도 개선 분야의 Kindling the Darkness(2019) 라는 논문의 코드를 수정한 것입니다 <br>
> Original Code Link : [github](https://github.com/zhangyhuaee/KinD)

<br><br>

* 요구사항
> Python
>
> Tensorflow >= 1.10.0
>
> numpy, PIL
<br>

* 바로 테스트 해보기 (저장된 체크포인트 파일로 즉시 test)
> $ python evaluate.py
<br>

* 모델 학습시키기 (3개의 서브넷 순서대로 train)
> $ python decomposition_net_train.py
> 
> $ python adjustment_net_train.py
> 
> $ python reflectance_restoration_net_train.py
<br>

---- 
<br>
현재 KinD Net의 업그레이드 버전인 KinD++ Net이 나와있습니다
KinD Net의 두번째 서브넷인 Reflectance Restoration Net의 성능을 개선해 전체 네트워크의 성능을 높인 모델입니다 
> Link : [github](https://github.com/zhangyhuaee/KinD_plus) 
<br>
