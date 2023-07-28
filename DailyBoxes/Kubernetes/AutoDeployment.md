## 1.7 自动化部署K8S（离线版）

### 1、 熟悉二进制部署K8S步骤

1. **服务器规划**

| **角色**                | **IP**                                 | **组件**                                                     |
| ----------------------- | -------------------------------------- | ------------------------------------------------------------ |
| k8s-master1             | 192.168.254.151                        | kube-apiserver  kube-controller-manager  kube-scheduler  etcd |
| k8s-master2             | 192.168.254.152                        | kube-apiserver  kube-controller-manager  kube-scheduler      |
| k8s-node1               | 192.168.254.153                        | kubelet  kube-proxy  docker  etcd                            |
| k8s-node2               | 192.168.254.154                        | kubelet  kube-proxy  docker  etcd                            |
| Load Balancer（Master） | 192.168.254.151  192.168.254.155 (VIP) | nginx  keepalived                                            |
| Load Balancer（Backup） | 192.168.254.152                        | nginx keepalived                                             |

2. **系统初始化**
   1. 关闭selinux，firewalld
   2. 关闭swap
   3. 时间同步
   4. 写hosts
3. **Etcd集群部署**
   1. 生成etcd证书
   2. 部署三个etcd集群
   3. 查看集群状态
4. **部署Master**
   1. 生成apiserver证书
   2. 部署apiserver、controller-manager和scheduler组件
   3. 启动TLS Bootstrapping
5. **部署Node**
   1. 安装Docker
   2. 部署kubelet和kube-proxy
   3. 在Master上允许为新Node颁发证书
   4. 授权apiserver访问kubelet
6. **部署插件（准备好镜像）**
   1. Flannel
   2. Web UI
   3. CoreDNS
   4. Ingress Controller
7. **Master高可用**
   1. 增加Master节点（与Master1一致）
   2. 部署Nginx负载均衡器
   3. Nginx+Keepalived高可用
   4. 修改Node连接VIP                            


### 2、Roles组织K8S各组件部署解析

编写建议：

1. 梳理流程和Roles结构
2. 如果配置文件有不固定内容，使用jinja渲染
3. 人工干预改动的内容应统一写到一个文件中

### 3、下载所需文件

> 确保所有节点系统时间一致

下载Ansible部署文件：

```
git clone https://github.com/lizhenliang/ansible-install-k8s
cd ansible-install-k8s
```

下载软件包并解压：

云盘地址：https://pan.baidu.com/s/1lTXolmlcCJbei9HY2BJRPQ

```
tar zxf binary_pkg.tar.gz
```

### 4、修改Ansible文件

修改hosts文件，根据规划修改对应IP和名称。

```
vi hosts
```

修改group_vars/all.yml文件，修改软件包目录和证书可信任IP。

```
vim group_vars/all.yml
software_dir: '/root/binary_pkg'
...
cert_hosts:
  k8s:
  etcd:
```

### 5、一键部署

**架构图**

![](https://k8s-1252881505.cos.ap-beijing.myqcloud.com/k8s-2/single-master.jpg)

​																				单Master架构


![avatar](https://k8s-1252881505.cos.ap-beijing.myqcloud.com/k8s-2/multi-master.jpg)

​																					多Master架构

**部署命令**
单Master版：

```
ansible-playbook -i hosts single-master-deploy.yml -uroot -k
```

多Master版：

```
ansible-playbook -i hosts multi-master-deploy.yml -uroot -k
```

### 6、部署控制

如果安装某个阶段失败，可针对性测试.

例如：只运行部署插件

```
ansible-playbook -i hosts single-master-deploy.yml -uroot -k --tags addons
```



示例参考：https://github.com/ansible/ansible-examples

