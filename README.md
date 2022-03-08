# rasa-component
使用方法，放入 rasa 目錄



rasa  language model featurizer 需要搭配任一的 tokenizer，這裡如果用 jieba 會出錯，因此採用 SpacyTokenizer 或自定義的 Tokenizer

```yaml
pipeline:
# ... Featurizer 前面必須搭配 tokenizer
   - name: "SpacyNLP"
     model: "zh_core_web_sm"
   - name: "SpacyTokenizer"
     "intent_tokenization_flag": False
     "intent_split_symbol": "_"
     "token_pattern": None
   - name: compoments.AlbertCompoments.AlbertFeaturizer
# ...
```



## SEE ALSO
- [Dustyposa/rasa_ch_faq at dev](https://github.com/Dustyposa/rasa_ch_faq/tree/dev)
- [howl-anderson/rasa_chinese: rasa_chinese 专门针对中文语言的 rasa 组件扩展包，提供了许多针对中文语言的组件](https://github.com/howl-anderson/rasa_chinese)
- [circlelychen/rukip: An Embedded CKIP Rasa NLU Components](https://github.com/circlelychen/rukip)
