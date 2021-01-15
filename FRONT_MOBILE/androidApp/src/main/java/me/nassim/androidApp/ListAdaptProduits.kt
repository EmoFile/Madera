package me.nassim.androidApp

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import androidx.appcompat.widget.AppCompatTextView

class ListAdaptProduits(val context: Context, val list: ArrayList<Produits>): BaseAdapter(){
    override fun getCount(): Int {
        return list.size
    }

    override fun getItem(position: Int): Any {
        return list[position]
    }

    override fun getItemId(position: Int): Long {
        return position.toLong()
    }

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view: View = LayoutInflater.from(context).inflate(R.layout.produits_layout,parent,false)

        val produitsId = view.findViewById(R.id.produits_id) as AppCompatTextView
        val produitsName = view.findViewById(R.id.produits_name) as AppCompatTextView

        produitsId.text = list[position].id.toString()
        produitsName.text = list[position].name

        return view
    }
}