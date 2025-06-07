# weichuanbiao 围串标


## 2025-06-02 Meeting notes
```text
explainable
metrics
no expectation
high precision
sort by high frequency
3. report frequency:
monthly?weekly?

data
CSV 4
SQL

Method
extend feature
join outer source
DNN

中标
唯一中标

规则：
同一IP 上传标书
投标文件上传IP
Mac 地址
投标上传时间

价格相似，主图标人价格低，影子高
共线关系：同一批公司重复参与竞标
同一批影子公司总是不中标
企查查
标书
```


## brainstorming
——————

1. cluster of companies
2. cluster over attributes
3. cluster overtime

### baseline 1

* sample1: company + attributes + historical attributes
* sample2: company + attributes + historical attributes

```
clustering algorithm
output: company + cluster id
```

#### problems:
1. how to automatically find cluster of attributes
2. how to cluster by attribute similarity
    * similar price
3. how to cluster by time
    * historical the same set of companies in the same cluster
4. how does LLM work in the framework