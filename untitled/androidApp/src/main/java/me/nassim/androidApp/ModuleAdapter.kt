package me.nassim.androidApp

import android.content.Context
import android.text.Editable
import android.text.TextWatcher
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.RelativeLayout
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import org.json.JSONArray
import org.json.JSONObject
import java.text.FieldPosition


class ModuleAdapter(private val context: Context, private val list: JSONArray) : BaseAdapter() {
    override fun getCount(): Int {
        return list.length()
    }

    override fun getItem(p0: Int): Any {
        return list.getJSONObject(p0)
    }

    override fun getItemId(p0: Int): Long {
        return p0.toLong()
    }

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view: View = LayoutInflater.from(context).inflate(R.layout.item_module_vertical, parent, false)

        val productName = view.findViewById<TextView>(R.id.module_name)
        val productPrice = view.findViewById<TextView>(R.id.module_price)
        val productNumber= view.findViewById<TextView>(R.id.editTextNumber)
        val item = list.getJSONObject(position)

        productName.text = item.getString("nom")
        productPrice.text = item.getInt("prix").toString()

        val mainGrandParent: View = parent?.parent?.parent?.parent?.parent?.parent as View
        val totalprice = mainGrandParent.findViewById<TextView>(R.id.price)
        totalprice.text = "36544"
        productNumber.text = "2"
        println((productNumber.text.toString().toInt() * productPrice.text.toString().toInt()).toString())


       /* productNumber.addTextChangedListener(
            object : TextWatcher {

                override fun afterTextChanged(s: Editable) {


                }

                override fun beforeTextChanged(s: CharSequence, start: Int,
                                               count: Int, after: Int) {
                }

                override fun onTextChanged(s: CharSequence, start: Int,
                                           before: Int, count: Int) {
                }
                )*/

        return view
    }
}