![1](https://user-images.githubusercontent.com/102397160/189475217-3d99c6e5-4162-4a70-a7f8-0a37ca124e3e.png)
![2](https://user-images.githubusercontent.com/102397160/189475219-29c39d5f-0ff4-45dd-936e-12bf8cad7681.png)


为了便于复制，代码放在下边了。

implementation(name: 'xwalk_shared_library-23.53.589.4', ext: 'aar')

flatDir { dirs './libs' }

xwalk_shared_library-23.53.589.4.aar 

文件在这个文件夹里：https://github.com/dlgt7/TVbox-interface/tree/main/xwalk_shared_library23.53.589.4


如果不用android_builder打包release版apk，则如下改动：

//    implementation('org.xwalk:xwalk_shared_library:23.53.589.4') {
//        exclude group: 'com.android.support'
//    } 屏蔽这些

implementation files('libs\\thunder.jar')
// 添加下边的
implementation files('libs\\xwalk_shared_library-23.53.589.4.aar')
