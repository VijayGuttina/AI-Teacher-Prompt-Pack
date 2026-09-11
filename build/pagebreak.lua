function Div(el)
  if el.classes:includes("pagebreak") then
    if FORMAT:match("docx") then
      return pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    elseif FORMAT:match("latex") or FORMAT:match("pdf") then
      return pandoc.RawBlock("latex", "\\newpage")
    end
  end
end
